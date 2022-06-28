function showPassword()
{
  document.getElementById('pass').type="text";
  setTimeout(() => {
    document.getElementById('pass').type="password";
  },2000);}
