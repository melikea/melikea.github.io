---
title: ""
permalink: /forwardinclusion/
layout: default
---

<style type="text/css" media="screen">
  .container {
    margin: 10px auto;
    text-align: center;
  }
  h1 {
    margin: 10px 0;
    font-size: 4em;
    line-height: 1;
    letter-spacing: -1px;
  }
</style>


<div class="container">
  <h2><strong>Forward inclusion functions for ray-tracing implicit surfaces</strong></h2>
  <h3> <a href="https://melikea.github.io">Melike Aydinlilar</a>, <a href="https://members.loria.fr/CZanni/">Cédric Zanni</a> <h3>
  <h3>Université de Lorraine, CNRS, Inria, LORIA</h3> 
  <h3>SMI 2023</h3>

<a href="../Preprint.pdf" download="ForwardInclusionSMI2023">Preprint</a>

  
<img src="../img/web_teaser.png">
  
  <h3><strong>Abstract</strong></h3>
  <p>Using Lipschitz bounds as linear inclusion functions, we show that both Lipschitz-based ray-tracing and bottom-up inclusion functions can be used together in the same framework. We propose asymmetrical forward inclusion functions that are exact at the query point and can better encode the function’s behavior on a given interval; therefore well suited for iterative processing. We show how to derive the linear and quadratic versions of these inclusion functions either by bounding the derivatives or building bottom-up inclusion functions and combining these two. We show our results on density fields defined from point primitives with compactly supported kernels and Gaussian kernels as well as Hermite radial basis functions. We demonstrate that our method provides noticeable improvement for grazing rays and transparent rendering.</p>

<img src="../img/tracing.png">

Comparison of the root finding behavior for the given ray configuration for the top left scene with two blobs.

<br><br>


<video controls>
<source src="../img/linear.mp4"  type="video/mp4">
Your browser does not support the video tag.
</video>

Video capture of the comparison between symmetric and asymmetric linear bounds, showing the improvement on the number of steps to converge to the surface. 
<br>
Demo : <a href="https://www.shadertoy.com/view/DdtczB" >www.shadertoy.com/view/DdtczB</a>

<br><br>


<section class="section" style="text-align:left" id="BibTeX">
      <h2  style="text-align:left">BibTeX</h2>
      <pre><code style="text-align:left">@article{aydinlilar23,
        TITLE = {Forward inclusion functions for ray-tracing implicit surfaces},
        AUTHOR = {Aydinlilar, Melike and Zanni, C{\'e}dric},
        URL = {https://inria.hal.science/hal-04129922},
        JOURNAL = {Computers and Graphics},
        PUBLISHER = {Elsevier},
        VOLUME = {114},
        PAGES = {190-200},
        YEAR = {2023},
        MONTH = Jun,
        DOI = {10.1016/j.cag.2023.05.026}
        }</code></pre>
  </section>














