module F30 (VV22V , VV29V , VV30V); 
input VV22V , VV29V;
output VV30V;
wire WW29W0W;

not f0 (WW29W0W , VV22V);
and f1 (VV30V , WW29W0W , VV29V);
endmodule