#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-vadrenaline.jarbasai=skill_vadrenaline:VAdrenalineSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-vadrenaline',
    version='0.0.1',
    description='ovos V Adrenaline skill plugin',
    url='https://github.com/JarbasSkills/skill-vadrenaline',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_vadrenaline": ""},
    package_data={'skill_vadrenaline': ['locale/*', 'res/*']},
    packages=['skill_vadrenaline'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
