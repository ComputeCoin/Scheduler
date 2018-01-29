"""
This module is the gateway between the scheduler and the cloud platform.
Any cloud data that the scheduler needs to access, will be requested
through this gateway, and sent back through this gateway.

This module contains the method of the form:
    (Scheduler requests CloudData) -> (Cloud returns CloudData)

Example:
    | Request            | Return                                           |
    | communication time | matrix with the corresponding communication times|
"""


def get_comm_matrix():
    pass