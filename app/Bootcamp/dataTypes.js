function DataTypes(arg){
  if(arg === undefined){
    var argument = "undefined";
  } else if(arg === null){
    var argument = "null"
  } else {
    var argument = typeof(arg)
  }
  switch(argument){
    case "string":
      return arg.length;
      break;
      
    case "boolean":
      return arg;
      break;
      
    case "number":
      if(arg<100){
        return 'less than 100';
      } else if (arg=100){
        return 'equal to 100';
      } else {
        return 'more than 100';
      }
      break;
      
    case "object":
      if(Array.isArray(arg)){
        if(arg[2]){
          return arg[2];
        }else{
          return undefined;
        }
      }
      break;
      
    case "function":
      return arg(true);
      break;
      
    default:
      if (argument==="null" || argument==="undefined")
        return 'no value';
      break;
  }
  
}