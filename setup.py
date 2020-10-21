# -*- coding: utf-8 -*-
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

path_version = path.join(here, 'spinalcordtoolbox', 'version.txt')
with open(path_version) as f:
    version = f.read().strip()

setup(
    name='spinalcordtoolbox',
    version=version,
    description='Library of analysis tools for MRI of the spinal cord',
    long_description=long_description,
    url='http://www.neuro.polymtl.ca/home',
    author='NeuroPoly Lab, Polytechnique Montreal',
    author_email='neuropoly@googlegroups.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='Magnetic Resonance Imaging MRI spinal cord analysis template',
    packages=find_packages(exclude=['.git', 'data', 'dev', 'dev.*', 'install', 'testing', 'build']),
    python_requires='>=3.6, <3.7',  # FIXME because tensorflow==1.5.0
    install_requires=['colored',
                      'dipy',
                      'futures',
                      'ivadomed==2.0.2',
                      'Keras==2.1.5',
                      'matplotlib',
                      'nibabel',
                      'numpy',
                      'pandas',
                      'psutil',
                      'pyqt5==5.11.3',
                      #   'raven', # unused?
                      'requests',
                      'scipy',
                      'tensorflow==1.5.0',
                      'torch==1.5.0',
                      'torchvision==0.6.0',
                      'xlwt',
                      'tqdm',
                      'transforms3d',
                      'urllib3[secure]',
                      ],
    extras_require={
        'docs': [
            'sphinx',
            'sphinxcontrib-programoutput',
            'sphinx_rtd_theme',
            'recommonmark'
        ],
        'mpi': [
            'mpich==3.2',
            'mpi4py==3.0.0',
        ],
        'dev': [
            'requirements-parser',
            'pytest_console_scripts',
            'pytest-xdist',
            'pytest',
            'pytest-cov',
        ]
    },
    entry_points={
        'console_scripts': [
            'isct_minc2volume_viewer=scripts.isct_minc2volume_viewer:main',
            'isct_test_ants=scripts.isct_test_ants:main',
            'sct_analyze_lesion=scripts.sct_analyze_lesion:main',
            'sct_analyze_texture=scripts.sct_analyze_texture:main',
            'sct_apply_transfo=scripts.sct_apply_transfo:main',
            'sct_check_dependencies=scripts.sct_check_dependencies:main',
            'sct_compute_ernst_angle=scripts.sct_compute_ernst_angle:main',
            'sct_compute_hausdorff_distance=scripts.sct_compute_hausdorff_distance:main',
            'sct_compute_mscc=scripts.sct_compute_mscc:main',
            'sct_compute_mtr=scripts.sct_compute_mtr:main',
            'sct_compute_mtsat=scripts.sct_compute_mtsat:main',
            'sct_compute_snr=scripts.sct_compute_snr:main',
            'sct_convert=scripts.sct_convert:main',
            'sct_create_mask=scripts.sct_create_mask:main',
            'sct_crop_image=scripts.sct_crop_image:main',
            'sct_deepseg=scripts.sct_deepseg:main',
            'sct_deepseg_gm=scripts.sct_deepseg_gm:main',
            'sct_deepseg_lesion=scripts.sct_deepseg_lesion:main',
            'sct_deepseg_sc=scripts.sct_deepseg_sc:main',
            'sct_denoising_onlm=scripts.sct_denoising_onlm:main',
            'sct_detect_pmj=scripts.sct_detect_pmj:main',
            'sct_dice_coefficient=scripts.sct_dice_coefficient:main',
            'sct_dmri_compute_bvalue=scripts.sct_dmri_compute_bvalue:main',
            'sct_dmri_compute_dti=scripts.sct_dmri_compute_dti:main',
            'sct_dmri_concat_b0_and_dwi=scripts.sct_dmri_concat_b0_and_dwi:main',
            'sct_dmri_concat_bvals=scripts.sct_dmri_concat_bvals:main',
            'sct_dmri_concat_bvecs=scripts.sct_dmri_concat_bvecs:main',
            'sct_dmri_display_bvecs=scripts.sct_dmri_display_bvecs:main',
            'sct_dmri_moco=scripts.sct_dmri_moco:main',
            'sct_dmri_separate_b0_and_dwi=scripts.sct_dmri_separate_b0_and_dwi:main',
            'sct_dmri_transpose_bvecs=scripts.sct_dmri_transpose_bvecs:main',
            'sct_download_data=scripts.sct_download_data:main',
            'sct_extract_metric=scripts.sct_extract_metric:main',
            'sct_flatten_sagittal=scripts.sct_flatten_sagittal:main',
            'sct_fmri_compute_tsnr=scripts.sct_fmri_compute_tsnr:main',
            'sct_fmri_moco=scripts.sct_fmri_moco:main',
            'sct_get_centerline=scripts.sct_get_centerline:main',
            'sct_image=scripts.sct_image:main',
            'sct_label_utils=scripts.sct_label_utils:main',
            'sct_label_vertebrae=scripts.sct_label_vertebrae:main',
            'sct_maths=scripts.sct_maths:main',
            'sct_merge_images=scripts.sct_merge_images:main',
            'sct_process_segmentation=scripts.sct_process_segmentation:main',
            'sct_run_batch=scripts.sct_run_batch:main',
            'sct_propseg=scripts.sct_propseg:main',
            'sct_qc=scripts.sct_qc:main',
            'sct_register_multimodal=scripts.sct_register_multimodal:main',
            'sct_register_to_template=scripts.sct_register_to_template:main',
            'sct_resample=scripts.sct_resample:main',
            'sct_smooth_spinalcord=scripts.sct_smooth_spinalcord:main',
            'sct_straighten_spinalcord=scripts.sct_straighten_spinalcord:main',
            'sct_testing=scripts.sct_testing:main',
            'sct_version=scripts.sct_version:main',
            'sct_warp_template=scripts.sct_warp_template:main',
        ],
    },

)
