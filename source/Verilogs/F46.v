module F46 (VV30V , VV45V , VV46V); 
input VV30V , VV45V;
output VV46V;
or f0 (VV46V , VV30V , VV45V);
endmodule