module F124 (VV120V , VV123V , VV124V); 
input VV120V , VV123V;
output VV124V;
xor f0 (VV124V , VV120V , VV123V);
endmodule