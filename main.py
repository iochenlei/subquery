import os
from mkdocs_git_revision_date_localized_plugin.util import Util


def define_env(env):
    @env.macro
    def newest_posts():
        results = []
        util = Util(env.variables.config)
        for page in env.variables.navigation.pages:
            if not page.url:
                continue
            revision_dates = util.get_revision_date_for_file(
                path=page.file.abs_src_path,
                locale='zh',
                time_zone='Asia/Shanghai',
                fallback_to_build_date=True,
            )
            revision_date = revision_dates['date']
            results.append((revision_date, page))
        results = sorted(results, key=lambda x: x[0], reverse=True)
        output = []
        for revision_date, page in results[:50]:
            output.append('+ ' + revision_date + ' - <a href="%s">%s</a>' % (page.abs_url, page.title))
        return "\n".join(output)
