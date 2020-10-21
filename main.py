import os
from datetime import datetime

def define_env(env):
    @env.macro
    def newest_posts():
        results = []
        for page in env.variables.navigation.pages:
            if not page.url:
                continue
            filename = os.path.join(env.variables.config['docs_dir'],
                page.url[:len(page.url) - 1] + '.md')
            results.append((os.stat(filename).st_mtime, page))
        results = sorted(results, key=lambda x: x[0], reverse=True)
        output = []
        for modify_time, page in results[:50]:
            output.append("+ " + datetime.fromtimestamp(modify_time).strftime("%Y-%m-%d %H:%M:%S") + " - <a href=\"" + page.abs_url + "\">" + page.title + "</a>")
        return "\n".join(output)
