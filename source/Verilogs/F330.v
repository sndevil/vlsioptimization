module F330 (VV314V , VV329V , VV330V); 
input VV314V , VV329V;
output VV330V;
xor f0 (VV330V , VV314V , VV329V);
endmodule