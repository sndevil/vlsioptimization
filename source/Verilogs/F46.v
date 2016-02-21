module F46 (VV30V , VV45V , VV46V); 
input VV30V , VV45V;
output VV46V;
wire WW45W0W;

not f0 (WW45W0W , VV30V);
and f1 (VV46V , WW45W0W , VV45V);
endmodule