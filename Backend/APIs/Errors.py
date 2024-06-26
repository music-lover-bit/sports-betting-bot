from enum import Enum


class Error(Enum):
    SUCCESS = 200
    ERR_FAILED_TO_PARSE_UPCOMING_EVENTS = -1
    ERR_FAILED_TO_GET_UPCOMING_EVENTS = -2
    ERR_FAILED_TO_GET_INPLAY_EVENTS = -3
    ERR_FAILED_TO_GET_VIEW_EVENT = -4
    ERR_FAILED_TO_GET_ENDED_EVENTS = -5
    ERR_ANOTHER = -2
    NOT_ENOUGH_BALANCE = -8
    AMOUNT_VALUE_ERROR = -9

