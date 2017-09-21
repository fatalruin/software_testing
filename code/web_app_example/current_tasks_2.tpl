%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  <td>TASK</td>
  <td contents="text">{{row[1]}}</td>
  <td contents="id">{{row[0]}}</td>
  </tr>
%end
</table>