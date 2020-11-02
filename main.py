import os
import time
from datetime import datetime
from babel.dates import get_timezone
from git import Repo
from collections import defaultdict


def _changlog(env):
    results = []
    repo_cache = {}

    def _get_repo(path: str):
        if not os.path.isdir(path):
            path = os.path.dirname(path)

        if path not in repo_cache:
            repo_cache[path] = Repo(path, search_parent_directories=True).git
        return repo_cache[path]

    for page in env.variables.navigation.pages:
        if not page.url:
            continue
        unix_timestamp = time.time()
        try:
            realpath = os.path.realpath(page.file.abs_src_path)
            repo = _get_repo(realpath)
            unix_timestamp = repo.log(realpath, n=1, date="short",
                                      format="%at")
            unix_timestamp = int(unix_timestamp)
        except Exception as e:
            print(e)
            pass
        results.append((unix_timestamp, page))
    results = sorted(results, key=lambda x: x[0], reverse=True)
    posts_group_by_month = defaultdict(list)
    ordered_keys = []

    for unix_timestamp, page in results[:50]:
        utc_revision_date = datetime.utcfromtimestamp(unix_timestamp)
        loc_revision_date = utc_revision_date.replace(tzinfo=get_timezone('UTC')) \
            .astimezone(get_timezone('Asia/Shanghai'))
        month_as_key = loc_revision_date.strftime('%Y年%m月')
        ordered_keys.append(month_as_key)
        post_update_datetime = loc_revision_date.strftime('%Y-%m-%d %H:%M:%S')
        posts_group_by_month[month_as_key].append('    + [%s] [%s](%s)' % (post_update_datetime, page.title, page.abs_url))

    output = []

    for key in ordered_keys:
        output.append("+ **" + key + "**")
        output.append("\n".join(posts_group_by_month[key]))
    return "\n".join(output)


def define_env(env):
    env.macro(lambda: _changlog(env), 'changelog')
