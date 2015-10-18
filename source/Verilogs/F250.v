module F250 (VV242V , VV249V , VV250V); 
input VV242V , VV249V;
output VV250V;
or f0 (VV250V , VV242V , VV249V);
endmodule