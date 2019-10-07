# Copyright 2019 Infuse Team
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import logging
import importlib

LOG = logging.getLogger(__name__)


def main(args):
    """Runner main entry."""
    Platform = getattr(importlib.import_module(
        "infraform.platforms.{}".format(args.platform)),
        args.platform.capitalize())
    platform = Platform(args=args)
    platform.prepare()
    platform.run()