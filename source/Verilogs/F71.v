module F71 (VV63V , VV70V , VV71V); 
input VV63V , VV70V;
output VV71V;
xor f0 (VV71V , VV63V , VV70V);
endmodule