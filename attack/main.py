from typing import Type

import requests


class LangCodes:
    Python = 48

class SubmitInfo:
    source_code: str
    lang_code: int
    prob_id: int
    space_id: int = 1

class BaseCommenter:
    def decorate_source(self, submit_info: SubmitInfo) -> SubmitInfo:
        raise NotImplementedError


class Submitter:
    API_ACTION = 'submit'
    def make_submit_files(self, submit_info: SubmitInfo, jid):
        files = {
            'Action': (None, 'submit'),
            'JudgeID': (None, jid),
            'Source': (None, submit_info.source_code),
            'Language': (None, submit_info.lang_code),
            'ProblemNum': (None, submit_info.prob_id),
            'SpaceID': (None, submit_info.space_id),
        }
        return files

    def send_submit(self, sub_info: SubmitInfo, jid):
        files = self.make_submit_files(sub_info, jid)
        return requests.post()







