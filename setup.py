#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-thoughtaudio.jarbasai=skill_thoughtaudio:ThoughtAudioSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-thoughtaudio',
    version='0.0.1',
    description='ovos thoughtaudio skill plugin',
    url='https://github.com/JarbasSkills/skill-thoughtaudio',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_thoughtaudio": ""},
    package_data={'skill_thoughtaudio': ['locale/*', 'res/*', 'ui/*']},
    packages=['skill_thoughtaudio'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
