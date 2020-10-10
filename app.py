#!/usr/bin/env python3

from aws_cdk import core

from awschallenge.awschallenge_stack import AwschallengeStack


app = core.App()
AwschallengeStack(app, "awschallenge", env={'region': 'us-west-2'})

app.synth()
