"""
sprite_sheet contains parameters
for the targetted sprite sheet:

 - name: sprite sheet filename should be in res folder
 - animaton_row: location of animation on sprite sheet
 - frame_count: number of frames in animation (sprites on row) 
 - row_count: total number of rows in the sprite sheet
"""
sprite_sheet = {
	"name": "example2.png",
	"animation_row": 3,
	"frame_count": 9,
	"row_count": 4
}

"""
animation_contains parameters of the animation window:

- width: desired window width in pixels
- height: desired window height in pixels
- background_color: desired backgound color as rgb tuple
"""
animation_window = {
	"width": 1000,
	"height": 200,
	"background_color": (255, 123, 255)
}