module F230 (c , d , VV230V); 
input c , d;
output VV230V;
xor f0 (VV230V , c , d);
endmodule