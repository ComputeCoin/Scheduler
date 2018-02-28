"""
This module is the gateway between the platform and scheduler. Any interaction
that the platform needs to make, with the scheduler will be done through this
module.

This module contains the method of the form:
    (Platform interacts with Scheduler) -> (Scheduler responds to Platform)

Example:
    | Interaction | Response                  |
    | Submit Job  | Admits job to the job pool|
"""


def submit(submission, input_type="job"):
    pass