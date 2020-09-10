
<pre><strong id="id1">format_spec    </strong> ::=  [[<a class="reference internal" href="#grammar-token-fill"><code class="xref docutils literal notranslate"><span class="pre">fill</span></code></a>]<a class="reference internal" href="#grammar-token-align"><code class="xref docutils literal notranslate"><span class="pre">align</span></code></a>][<a class="reference internal" href="#grammar-token-sign"><code class="xref docutils literal notranslate"><span class="pre">sign</span></code></a>][#][0][<a class="reference internal" href="#grammar-token-width"><code class="xref docutils literal notranslate"><span class="pre">width</span></code></a>][<a class="reference internal" href="#grammar-token-grouping-option"><code class="xref docutils literal notranslate"><span class="pre">grouping_option</span></code></a>][.<a class="reference internal" href="#grammar-token-precision"><code class="xref docutils literal notranslate"><span class="pre">precision</span></code></a>][<a class="reference internal" href="#grammar-token-type"><code class="xref docutils literal notranslate"><span class="pre">type</span></code></a>]
<strong id="grammar-token-fill">fill           </strong> ::=  &lt;any character&gt;
<strong id="grammar-token-align">align          </strong> ::=  "&lt;" | "&gt;" | "=" | "^"
<strong id="grammar-token-sign">sign           </strong> ::=  "+" | "-" | " "
<strong id="grammar-token-width">width          </strong> ::=  <a class="reference internal" href="../reference/lexical_analysis.html#grammar-token-digit"><code class="xref docutils literal notranslate"><span class="pre">digit</span></code></a>+
<strong id="grammar-token-grouping-option">grouping_option</strong> ::=  "_" | ","
<strong id="grammar-token-precision">precision      </strong> ::=  <a class="reference internal" href="../reference/lexical_analysis.html#grammar-token-digit"><code class="xref docutils literal notranslate"><span class="pre">digit</span></code></a>+
<strong id="grammar-token-type">type           </strong> ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
</pre>


<blockquote>
<div><table class="docutils align-default" id="index-3">
<colgroup>
<col style="width: 13%">
<col style="width: 87%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Option</p></th>
<th class="head"><p>Meaning</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'&lt;'</span></code></p></td>
<td><p>Forces the field to be left-aligned within the available
space (this is the default for most objects).</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'&gt;'</span></code></p></td>
<td><p>Forces the field to be right-aligned within the
available space (this is the default for numbers).</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'='</span></code></p></td>
<td><p>Forces the padding to be placed after the sign (if any)
but before the digits.  This is used for printing fields
in the form ‘+000000120’. This alignment option is only
valid for numeric types.  It becomes the default when ‘0’
immediately precedes the field width.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'^'</span></code></p></td>
<td><p>Forces the field to be centered within the available
space.</p></td>
</tr>
</tbody>
</table>
</div></blockquote>


