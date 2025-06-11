"""
ComfyUI Image Size Tool

A node pack providing resolution calculators for AI image generation models.
Includes optimized presets for SD 1.5, SDXL, and Flux.1 Dev with proper
validation and bucket-aware resolution selection.
"""

import os
import sys

# Ensure the current package directory is in sys.path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from nodes.sd15_resolution_node import SD15ResolutionNode
from nodes.sdxl_resolution_node import SDXLResolutionNode  
from nodes.flux_resolution_node import FluxResolutionNode

# Combine all node class mappings
NODE_CLASS_MAPPINGS = {
    "SD15ResolutionNode": SD15ResolutionNode,
    "SDXLResolutionNode": SDXLResolutionNode,
    "FluxResolutionNode": FluxResolutionNode,
}

# Combine all display name mappings
NODE_DISPLAY_NAME_MAPPINGS = {
    "SD15ResolutionNode": "SD 1.5 Resolution",
    "SDXLResolutionNode": "SDXL Resolution", 
    "FluxResolutionNode": "Flux.1 Dev Resolution",
}

# Export for ComfyUI
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]