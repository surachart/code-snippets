# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup dependencies for cloud deployment."""
import setuptools

if __name__ == '__main__':
  setuptools.setup(name='taxi_schema', version='1.0',
                   packages=setuptools.find_packages(),
                   install_requires=[
                       'jupyter==1.0',
                       'tensorflow==1.6.0',
                       'tensorflow-model-analysis==0.6.0',
                       'tensorflow-serving-api==1.6.0',
                       'tensorflow-transform==0.6.0'])
