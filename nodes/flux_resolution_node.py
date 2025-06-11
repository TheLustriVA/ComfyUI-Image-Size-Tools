import os
import sys

# Add the current package path to sys.path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
package_dir = os.path.dirname(current_dir)
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

from utils.resolution_data import FLUX_RESOLUTIONS, validate_resolution, get_aspect_ratio_text

class FluxResolutionNode:
    """
    Flux.1 Dev Resolution Calculator
    
    Provides practical resolution presets for Flux.1 Dev models.
    No strict divisibility requirements, focused on hardware compatibility
    and common use cases from 1024x1024 to 2560x1440.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution": (list(FLUX_RESOLUTIONS.keys()),),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "aspect_ratio")
    FUNCTION = "get_resolution"
    CATEGORY = "Image Size Tool"
    
    def get_resolution(self, resolution):
        """Get width, height, and aspect ratio for selected Flux.1 Dev resolution"""
        res_data = FLUX_RESOLUTIONS[resolution]
        width = res_data["width"]
        height = res_data["height"]
        aspect_ratio = res_data["ratio"]
        
        # Validate the resolution (Flux is more flexible)
        is_valid, message = validate_resolution(width, height, "FLUX")
        if not is_valid:
            print(f"Warning: Invalid resolution {width}×{height}: {message}")
        
        return (width, height, aspect_ratio)

# Node registration will be handled in __init__.py
NODE_CLASS_MAPPINGS = {
    "FluxResolutionNode": FluxResolutionNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FluxResolutionNode": "Flux.1 Dev Resolution"
}