use WWW::Mechanize;
use strict;
use warnings;
use HTTP::Cookies;
use IO::Socket::SSL;

#Restricting the available ciphers in IO::Socket::SSL
# results in a successsful handshake with the site.
IO::Socket::SSL::set_defaults(SSL_cipher_list => 'ALL:!3DES:!DES:!ADH:!SRP:!AESGCM:!SHA256:!SHA384');
my $outfile = "out.htm";
my $username = 'elliot';
my $password = '*****';
my $url = 'https://www.gradesource.com/login.asp';

my $mech = WWW::Mechanize->new;

#$mech->cookie_jar(HTTP::Cookies->new());
$mech->get($url);
$mech->form_name('loginForm');
$mech->field("User", $username);
$mech->field("Password", $password);
$mech->click();
my $output_page = $mech->content();
print $output_page;


open(OUTFILE, ">$outfile");
binmode(OUTFILE, ":utf8");
print OUTFILE "$output_page";
close(OUTFILE);

