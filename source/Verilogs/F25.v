module F25 (VV23V , VV24V , VV25V); 
input VV23V , VV24V;
output VV25V;
xor f0 (VV25V , VV23V , VV24V);
endmodule