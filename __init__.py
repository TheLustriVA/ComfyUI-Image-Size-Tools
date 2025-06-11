"""
ComfyUI Image Size Tool

A node pack providing resolution calculators for AI image generation models.
Includes optimized presets for SD 1.5, SDXL, and Flux.1 Dev with proper
validation and bucket-aware resolution selection.
"""

from .nodes.sd15_resolution_node import SD15ResolutionNode
from .nodes.sdxl_resolution_node import SDXLResolutionNode  
from .nodes.flux_resolution_node import FluxResolutionNode

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