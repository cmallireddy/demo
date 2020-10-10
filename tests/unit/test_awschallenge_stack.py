import json
import pytest

from aws_cdk import core
from awschallenge.awschallenge_stack import AwschallengeStack


def get_template():
    app = core.App()
    AwschallengeStack(app, "awschallenge")
    return json.dumps(app.synth().get_stack("awschallenge").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
