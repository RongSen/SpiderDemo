#coding:utf8

import bs4

from bs4 import BeautifulSoup

html = """
<ul>
<li><a href="#Quick%20Start">快速开始</a></li>
<li><a href="#Parsing%20a%20Document">剖析文档</a></li>
<ul>
<li><a href="#Parsing%20HTML">剖析 HTML</a></li>
<li><a href="#Parsing%20XML">剖析 XML</a></li>
<li><a href="#If%20That%20Doesn%27t%20Work">如果它不工作</a></li>
</ul>
<li><a href="#Beautiful%20Soup%20Gives%20You%20Unicode,%20Dammit">使用Unicode的Beautiful Soup, Dammit</a></li>
<li><a href="#Printing%20a%20Document">输出文档</a></li>
<li><a href="#The%20Parse%20Tree">剖析树</a></li>
<ul>
<li><a href="#The%20attributes%20of%20Tags"><code>Tag</code>s的属性</a></li>
</ul>
<li><a href="#Navigating%20the%20Parse%20Tree">Navigating 剖析树</a></li>
<ul>
<li><a href="#parent"><code>parent</code></a></li>
<li><a href="#contents"><code>contents</code></a></li>
<li><a href="#string"><code>string</code></a></li>
<li><a href="#nextSibling%20and%20previousSibling"><code>nextSibling</code> and <code>previousSibling</code></a></li>
<li><a href="#next%20and%20previous"><code>next</code> and <code>previous</code></a></li>
<li><a href="#Iterating%20over%20a%20Tag">遍历<code>Tag</code></a></li>
<li><a href="#Using%20tag%20names%20as%20members">使用标签名作为成员</a></li>
</ul>
<li><a href="#Searching%20the%20Parse%20Tree">Searching 剖析树</a></li>
<ul>
<li><a href="#The%20basic%20find%20method:%20findAll%28name,%20attrs,%20recursive,%20text,%20limit,%20**kwargs%29">The basic find method: <code>findAll(name, attrs, recursive, text, limit, **kwargs)</code></a></li>
<ul>
<li><a href="#Searching%20by%20CSS%20class">使用CSS类查找</a></li>
<li><a href="#Calling%20a%20tag%20is%20like%20calling%20findall">像 <code>findall</code>一样调用tag</a></li>
</ul>
<li><a href="#find%28name,%20attrs,%20recursive,%20text,%20**kwargs%29"><code>find(name, attrs, recursive, text, **kwargs)</code></a></li>
<li><a href="#What%20happened%20to%20first?"><code>first</code>哪里去了?</a></li>
</ul>
<li><a href="#Searching%20Within%20the%20Parse%20Tree">Searching 剖析树内部</a></li>
<ul>
<li><a href="#findNextSiblings%28name,%20attrs,%20text,%20limit,%20**kwargs%29%20and%20findNextSibling%28name,%20attrs,%20text,%20**kwargs%29"><code>findNextSiblings(name, attrs, text, limit, **kwargs)</code> and <code>findNextSibling(name, attrs, text, **kwargs)</code></a></li>
<li><a href="#findPreviousSiblings%28name,%20attrs,%20text,%20limit,%20**kwargs%29%20and%20findPreviousSibling%28name,%20attrs,%20text,%20**kwargs%29"><code>findPreviousSiblings(name, attrs, text, limit, **kwargs)</code> and <code>findPreviousSibling(name, attrs, text, **kwargs)</code></a></li>
<li><a href="#findAllNext%28name,%20attrs,%20text,%20limit,%20**kwargs%29%20and%20findNext%28name,%20attrs,%20text,%20**kwargs%29"><code>findAllNext(name, attrs, text, limit, **kwargs)</code> and <code>findNext(name, attrs, text, **kwargs)</code></a></li>
<li><a href="#findAllPrevious%28name,%20attrs,%20text,%20limit,%20**kwargs%29%20and%20findPrevious%28name,%20attrs,%20text,%20**kwargs%29"><code>findAllPrevious(name, attrs, text, limit, **kwargs)</code> and <code>findPrevious(name, attrs, text, **kwargs)</code></a></li>
</ul>
<li><a href="#Modifying%20the%20Parse%20Tree">Modifying 剖析树</a></li>
<ul>
<li><a href="#Changing%20attribute%20values">改变属性值</a></li>
<li><a href="#Removing%20elements">删除元素</a></li>
<li><a href="#Replacing%20one%20Element%20with%20Another">替换元素</a></li>
<li><a href="#Adding%20a%20Brand%20New%20Element">添加新元素</a></li>
</ul>
<li><a href="#Troubleshooting">常见问题(Troubleshooting)</a></li>
<ul>
<li><a href="#Why%20can%27t%20Beautiful%20Soup%20print%20out%20the%20non-ASCII%20characters%20I%20gave%20it?">为什么Beautiful Soup不能打印我的no-ASCII字符?</a></li>
<li><a href="#Beautiful%20Soup%20loses%20the%20data%20I%20fed%20it%21%20Why?%20WHY?????">Beautiful Soup 弄丢了我给的数据!为什么?为什么?????</a></li>
<li><a href="#Beautiful%20Soup%20is%20too%20slow%21">Beautiful Soup 太慢了!</a></li>
</ul>
<li><a href="#Advanced%20Topics">高级主题</a></li>
<ul>
<li><a href="#Generators">产生器(Generators)</a></li>
<li><a href="#Other%20Built-In%20Parsers">其他的内部剖析器</a></li>
<li><a href="#Customizing%20the%20Parser">定制剖析器(Parser)</a></li>
<li><a href="#Entity%20Conversion">实体转换</a></li>
<li><a href="#Sanitizing%20Bad%20Data%20with%20Regexps">使用正则式处理糟糕的数据</a></li>
<li><a href="#Fun%20With%20SoupStrainers">玩玩<code>SoupStrainer</code>s</a></li>
<li><a href="#Improving%20Performance%20by%20Parsing%20Only%20Part%20of%20the%20Document">通过剖析部分文档来提升效率</a></li>
<li><a href="#Improving%20Memory%20Usage%20with%20extract">使用<code>extract</code>改进内存使用</a></li>
</ul>
<li><a href="#See%20Also">其它</a></li>
<ul>
<li><a href="#Applications%20that%20use%20Beautiful%20Soup">使用Beautiful Soup的其他应用</a></li>
<li><a href="#Similar%20libraries">类似的库</a></li>
</ul>
<li><a href="#Conclusion">小结</a></li>
</ul>"""

soup = BeautifulSoup(html, 'html.parser', from_encoding="utf-8")

print('获取所有的链接')
links = soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()

