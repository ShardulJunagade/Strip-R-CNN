# dataset settings
dataset_type = 'BrickKilnDataset'
data_root = '/home/shardul.junagade/my-work/domain-adaptation-brick-kilns/data/' 
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='RResize', img_scale=(640, 640)),
    dict(type='RRandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels'])
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(640, 640),
        flip=False,
        transforms=[
            dict(type='RResize'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='DefaultFormatBundle'),
            dict(type='Collect', keys=['img'])
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=4,
    train=dict(
        type=dataset_type,
        ann_file=data_root + 'bihar_same_class_count_10_120_1000/annfiles/',
        img_prefix=data_root + 'bihar_same_class_count_10_120_1000/images_png/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'bihar_same_class_count_10_120_1000/annfiles/',
        img_prefix=data_root + 'bihar_same_class_count_10_120_1000/images_png/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'test_bihar_same_class_count_10_120_1000/images_png/',
        img_prefix=data_root + 'test_bihar_same_class_count_10_120_1000/images_png/',
        pipeline=test_pipeline))
