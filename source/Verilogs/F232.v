module F232 (VV230V , VV231V , VV232V); 
input VV230V , VV231V;
output VV232V;
and f0 (VV232V , VV230V , VV231V);
endmodule