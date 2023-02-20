# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

"""Pre-trained ResNet models."""

from typing import Any, Optional

import kornia.augmentation as K
import timm
import torch
from timm.models import ResNet
from torchvision.models._api import Weights, WeightsEnum

from ..transforms import AugmentationSequential

__all__ = ["ResNet50_Weights", "ResNet18_Weights"]


# https://github.com/zhu-xlab/SSL4EO-S12/blob/d2868adfada65e40910bfcedfc49bc3b20df2248/src/benchmark/transfer_classification/linear_BE_moco.py#L167 # noqa: E501
# https://github.com/zhu-xlab/SSL4EO-S12/blob/d2868adfada65e40910bfcedfc49bc3b20df2248/src/benchmark/transfer_classification/datasets/EuroSat/eurosat_dataset.py#L97 # noqa: E501
# Normalization either by 10K or channel-wise with band statistics
_zhu_xlab_transforms = AugmentationSequential(
    K.Resize(256),
    K.CenterCrop(224),
    K.Normalize(mean=0, std=10000),
    data_keys=["image"],
)

# https://github.com/ServiceNow/seasonal-contrast/blob/8285173ec205b64bc3e53b880344dd6c3f79fa7a/datasets/bigearthnet_dataset.py#L13 # noqa: E501
_seco_transforms = AugmentationSequential(
    K.Resize(128),
    K.Normalize(
        mean=torch.Tensor(
            [
                340.76769064,
                429.9430203,
                614.21682446,
                590.23569706,
                950.68368468,
                1792.46290469,
                2075.46795189,
                2218.94553375,
                2266.46036911,
                2246.0605464,
                1594.42694882,
                1009.32729131,
            ]
        ),
        std=torch.Tensor(
            [
                554.81258967,
                572.41639287,
                582.87945694,
                675.88746967,
                729.89827633,
                1096.01480586,
                1273.45393088,
                1365.45589904,
                1356.13789355,
                1302.3292881,
                1079.19066363,
                818.86747235,
            ]
        ),
    ),
    data_keys=["image"],
)

# https://github.com/pytorch/vision/pull/6883
# https://github.com/pytorch/vision/pull/7107
# Can be removed once torchvision>=0.15 is required
Weights.__deepcopy__ = lambda *args, **kwargs: args[0]


class ResNet18_Weights(WeightsEnum):  # type: ignore[misc]
    """ResNet18 weights.

    For `timm <https://github.com/rwightman/pytorch-image-models>`_
    *resnet18* implementation.

    .. versionadded:: 0.4
    """

    SENTINEL2_ALL_MOCO = Weights(
        url="https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",  # noqa: E501
        transforms=_zhu_xlab_transforms,
        meta={
            "dataset": "SSL4EO-S12",
            "in_chans": 13,
            "model": "resnet18",
            "publication": "https://arxiv.org/abs/2211.07044",
            "repo": "https://github.com/zhu-xlab/SSL4EO-S12",
            "ssl_method": "moco",
        },
    )

    SENTINEL2_RGB_MOCO = Weights(
        url="https://huggingface.co/torchgeo/resnet18_sentinel2_rgb_moco/resolve/main/resnet18_sentinel2_rgb_moco-e3a335e3.pth",  # noqa: E501
        transforms=_zhu_xlab_transforms,
        meta={
            "dataset": "SSL4EO-S12",
            "in_chans": 3,
            "model": "resnet18",
            "publication": "https://arxiv.org/abs/2211.07044",
            "repo": "https://github.com/zhu-xlab/SSL4EO-S12",
            "ssl_method": "moco",
        },
    )

    SENTINEL2_RGB_SECO = Weights(
        url="https://huggingface.co/torchgeo/resnet18_sentinel2_rgb_seco/resolve/main/resnet18_sentinel2_rgb_seco-9976a9cb.pth",  # noqa: E501
        transforms=_seco_transforms,
        meta={
            "dataset": "SeCo Dataset",
            "in_chans": 3,
            "model": "resnet18",
            "publication": "https://arxiv.org/abs/2103.16607",
            "repo": "https://github.com/ServiceNow/seasonal-contrast",
            "ssl_method": "seco",
        },
    )


class ResNet50_Weights(WeightsEnum):  # type: ignore[misc]
    """ResNet50 weights.

    For `timm <https://github.com/rwightman/pytorch-image-models>`_
    *resnet50* implementation.

    .. versionadded:: 0.4
    """

    SENTINEL1_ALL_MOCO = Weights(
        url="https://huggingface.co/torchgeo/resnet50_sentinel1_all_moco/resolve/main/resnet50_sentinel1_all_moco-906e4356.pth",  # noqa: E501
        transforms=_zhu_xlab_transforms,
        meta={
            "dataset": "SSL4EO-S12",
            "in_chans": 2,
            "model": "resnet50",
            "publication": "https://arxiv.org/abs/2211.07044",
            "repo": "https://github.com/zhu-xlab/SSL4EO-S12",
            "ssl_method": "moco",
        },
    )

    SENTINEL2_ALL_DINO = Weights(
        url="https://huggingface.co/torchgeo/resnet50_sentinel2_all_dino/resolve/main/resnet50_sentinel2_all_dino-d6c330e9.pth",  # noqa: E501
        transforms=_zhu_xlab_transforms,
        meta={
            "dataset": "SSL4EO-S12",
            "in_chans": 13,
            "model": "resnet50",
            "publication": "https://arxiv.org/abs/2211.07044",
            "repo": "https://github.com/zhu-xlab/SSL4EO-S12",
            "ssl_method": "dino",
        },
    )

    SENTINEL2_ALL_MOCO = Weights(
        url="https://huggingface.co/torchgeo/resnet50_sentinel2_all_moco/resolve/main/resnet50_sentinel2_all_moco-df8b932e.pth",  # noqa: E501
        transforms=_zhu_xlab_transforms,
        meta={
            "dataset": "SSL4EO-S12",
            "in_chans": 13,
            "model": "resnet50",
            "publication": "https://arxiv.org/abs/2211.07044",
            "repo": "https://github.com/zhu-xlab/SSL4EO-S12",
            "ssl_method": "moco",
        },
    )

    SENTINEL2_RGB_MOCO = Weights(
        url="https://huggingface.co/torchgeo/resnet50_sentinel2_rgb_moco/resolve/main/resnet50_sentinel2_rgb_moco-2b57ba8b.pth",  # noqa: E501
        transforms=_zhu_xlab_transforms,
        meta={
            "dataset": "SSL4EO-S12",
            "in_chans": 3,
            "model": "resnet50",
            "publication": "https://arxiv.org/abs/2211.07044",
            "repo": "https://github.com/zhu-xlab/SSL4EO-S12",
            "ssl_method": "moco",
        },
    )

    SENTINEL2_RGB_SECO = Weights(
        url="https://huggingface.co/torchgeo/resnet50_sentinel2_rgb_seco/resolve/main/resnet50_sentinel2_rgb_seco-584035db.pth",  # noqa: E501
        transforms=_seco_transforms,
        meta={
            "dataset": "SeCo Dataset",
            "in_chans": 3,
            "model": "resnet50",
            "publication": "https://arxiv.org/abs/2103.16607",
            "repo": "https://github.com/ServiceNow/seasonal-contrast",
            "ssl_method": "seco",
        },
    )


def resnet18(
    weights: Optional[ResNet18_Weights] = None, *args: Any, **kwargs: Any
) -> ResNet:
    """ResNet-18 model.

    If you use this model in your research, please cite the following paper:

    * https://arxiv.org/pdf/1512.03385.pdf

    .. versionadded:: 0.4

    Args:
        weights: Pre-trained model weights to use.
        *args: Additional arguments to pass to :func:`timm.create_model`
        **kwargs: Additional keywork arguments to pass to :func:`timm.create_model`

    Returns:
        A ResNet-18 model.
    """
    if weights:
        kwargs["in_chans"] = weights.meta["in_chans"]

    model: ResNet = timm.create_model("resnet18", *args, **kwargs)

    if weights:
        model.load_state_dict(weights.get_state_dict(progress=True), strict=False)

    return model


def resnet50(
    weights: Optional[ResNet50_Weights] = None, *args: Any, **kwargs: Any
) -> ResNet:
    """ResNet-50 model.

    If you use this model in your research, please cite the following paper:

    * https://arxiv.org/pdf/1512.03385.pdf

    .. versionchanged:: 0.4
       Switched to multi-weight support API.

    Args:
        weights: Pre-trained model weights to use.
        *args: Additional arguments to pass to :func:`timm.create_model`.
        **kwargs: Additional keywork arguments to pass to :func:`timm.create_model`.

    Returns:
        A ResNet-50 model.
    """
    if weights:
        kwargs["in_chans"] = weights.meta["in_chans"]

    model: ResNet = timm.create_model("resnet50", *args, **kwargs)

    if weights:
        model.load_state_dict(weights.get_state_dict(progress=True), strict=False)

    return model
