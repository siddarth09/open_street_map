# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, LaunchIntrospector, LaunchService
from launch_ros import actions, get_default_launch_description


def generate_launch_description():
    """
    Launch file for visualizing OSM data
    """
    map_url = "file://"+os.path.join(get_package_share_directory("osm_cartography"), "tests", "prc.osm")

    # Start map server
    osm_server = actions.Node(
        package='osm_cartography', node_executable='osm_server', output='screen')

    # Start map visualization
    viz_osm = actions.Node(
        package='osm_cartography', node_executable='viz_osm', output='screen',
        parameters=[{"map_url": map_url}])

    return LaunchDescription([osm_server, viz_osm])


def main():
    ld = generate_launch_description()

    ls = LaunchService()
    ls.include_launch_description(get_default_launch_description())
    ls.include_launch_description(ld)
    return ls.run()


if __name__ == '__main__':
    main()
