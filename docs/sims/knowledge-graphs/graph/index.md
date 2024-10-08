# Circuits Course Concept Dependency Graph

[HTML Page for Dependency Graph](./dep-graph.html)

## Adjusting Visualization

In the [JavaScript](script.js) file you can change the display options.
Here is the portion of the JavaScript that changes the options.

```js
var options = {
    nodes: {
        shape: 'dot',
        size: 10,
        font: {
            size: 14,
        },
    },
    edges: {
        arrows: 'to',
        smooth: true,
    },
    physics: {
        stabilization: false,
    },
};
```

## Left to Right Layout

[HTML Page for Dependency Graph](./lr-layout.html)

```js
var options = {
layout: {
        hierarchical: {
          direction: 'LR',  // Left to right
          sortMethod: 'directed',  // Sort nodes based on dependencies
          nodeSpacing: 200,  // Adjust spacing if needed
          levelSeparation: 150  // Adjust for horizontal space between levels
        }
      }
}
```

## Full Layout Options

```js
layout: {
    randomSeed: undefined,
    improvedLayout:true,
    clusterThreshold: 150,
    hierarchical: {
      enabled:false,
      levelSeparation: 150,
      nodeSpacing: 100,
      treeSpacing: 200,
      blockShifting: true,
      edgeMinimization: true,
      parentCentralization: true,
      direction: 'LR',        // UD, DU, LR, RL
      sortMethod: 'hubsize',  // hubsize, directed
      shakeTowards: 'leaves'  // roots, leaves
    }
  }
  ```

## Hierarchical Layout User Defined
https://visjs.github.io/vis-network/examples/network/layout/hierarchicalLayoutUserdefined.html

```js
  var options = {
          edges: {
            smooth: {
              type: "cubicBezier",
              forceDirection:
                directionInput.value == "UD" || directionInput.value == "DU"
                  ? "vertical"
                  : "horizontal",
              roundness: 0.4,
            },
          },
          layout: {
            hierarchical: {
              direction: directionInput.value,
            },
          },
          physics: false,
        };
```

## Category Colors

We can use generative AI to categorize each concept.
Here are 11 categories of the concepts

| CategoryID | Color  | CategoryLabel                                |
|------------|--------|----------------------------------------------|
| 1          | red    | Fundamental Concepts                         |
| 2          | orange | Passive Components                           |
| 3          | yellow | Active Components and Semiconductor Devices  |
| 4          | green  | Circuit Analysis Techniques                  |
| 5          | cyan   | AC Circuit Concepts                          |
| 6          | blue   | Transient Analysis                           |
| 7          | purple | Signal Processing and Filters                |
| 8          | pink   | Amplifiers and Analog Circuits               |
| 9          | gray   | Power Electronics                            |
| 10         | olive  | Control Systems and Stability                |
| 11         | brown  | Types of Circuits                            |


[Category Colors Demo](./category-colors.html)

[Cat Colors V3 DEBUG](./cat-colors-3.html)

## Reference

[Vis.js Network Layout Methods](https://visjs.github.io/vis-network/docs/network/#methodLayout)