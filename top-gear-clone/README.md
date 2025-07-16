This is a clone of the top gear game for SNES.
Implement a 2d-racing game that fakes depth by dynamically scaling and drawing rows of road sprites. Each slice of road is a sprite or tile whose width is increased or decreased per scanline to simulate perspective, and successive strips are drawn from the horizon toward the player to build the road surface.
Use one background layer for distant scenery (sky, mountains). 
Places the road strips and roadside objects (trees, signposts) as sprites on a second layer. 
Static HUD elements (speedometer, timer) live on yet another layer.