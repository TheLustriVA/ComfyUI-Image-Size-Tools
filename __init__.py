"""
ComfyUI Image Size Tool

A node pack providing resolution calculators for AI image generation models.
Includes optimized presets for SD 1.5, SDXL, and Flux.1 Dev with proper
validation and bucket-aware resolution selection.
"""

import os
import sys

# Ensure the current package directory is in sys.path for imports  
current_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import node modules directly using importlib to avoid namespace conflicts
import importlib.util

# Load SD15 Resolution Node
spec = importlib.util.spec_from_file_location("sd15_resolution_node", 
    os.path.join(current_dir, "nodes", "sd15_resolution_node.py"))
sd15_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sd15_module)
SD15ResolutionNode = sd15_module.SD15ResolutionNode

# Load SDXL Resolution Node  
spec = importlib.util.spec_from_file_location("sdxl_resolution_node",
    os.path.join(current_dir, "nodes", "sdxl_resolution_node.py"))
sdxl_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sdxl_module)
SDXLResolutionNode = sdxl_module.SDXLResolutionNode

# Load Flux Resolution Node
spec = importlib.util.spec_from_file_location("flux_resolution_node",
    os.path.join(current_dir, "nodes", "flux_resolution_node.py"))
flux_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(flux_module)
FluxResolutionNode = flux_module.FluxResolutionNode

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