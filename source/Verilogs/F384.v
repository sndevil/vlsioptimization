module F384 (VV380V , VV383V , VV384V); 
input VV380V , VV383V;
output VV384V;
and f0 (VV384V , VV380V , VV383V);
endmodule