#!/usr/bin/env python
# This is the main script for creating a PagerDuty report

import logging
import argparse
import datetime as dt
from collections import defaultdict

# read a config file to retrieve the domain
