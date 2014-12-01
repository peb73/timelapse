module panel_socle()
{

module extrude(coord)
{
	translate(coord){
			translate([0,0,-1]){
				union(){
					translate([0,0,4]){
						cube([112,135,20],false);
					};
					translate([12,12,0]){
						cube([88,111,20],false);
					};
					translate([8,8,0]){
						cylinder(20,1);
					};
					translate([104,8,0]){
						cylinder(20,1);
					};
					translate([8,128,0]){
						cylinder(20,1);
					};
					translate([104,128,0]){
						cylinder(20,1);
					};
				};
			}
		};
	}

	rayon = 2;
	difference(){
		minkowski()
		{
			cube(size=[232,139,4], center=false);
			cylinder(rayon,h=2);
		}
		extrude([2,2,0]);
		extrude([2+112+4, 2, 0]);
	}

};

panel_socle();



