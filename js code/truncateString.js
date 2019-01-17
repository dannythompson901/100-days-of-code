function truncateString(str, num) {
  var len = str.length;
  var a ="";
  if(num<len)
  {if(num<=3)
    {
      str = str.slice(0, num);
      str = str.concat(a);
      
    }
  else
    {
      str = str.slice(0,num-3);
      str = str.concat(a);
      
    }
  }
  return str;
}

truncateString("A-tisket a-tasket A green and yellow basket", 11);