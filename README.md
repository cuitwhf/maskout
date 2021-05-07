# maskout

This is a python process.

# Parameters 

***Param*** ax: Which the axes you want to mask out.

***Param*** shp_path: You should provide the region as the mask. **This shapefile must be asked for containing only one region.**

# Example

When not use the maskout. You will get a picture like this.

```
im = ax.contourf(x, y, z, bounds, extend='both', cmap=cmaps.WhBlGrYeRe)

# maskout(ax, r'D:\Ubuntu\WRF-Data\CDE\Shp-SCB\SCB-boundary.shp')
```

![image](https://github.com/cuitwhf/maskout/blob/main/WithoutMaskout.png)

When you use the maskout. You will get a picture like this.

```
im = ax.contourf(x, y, z, bounds, extend='both', cmap=cmaps.WhBlGrYeRe)

maskout(ax, r'D:\Ubuntu\WRF-Data\CDE\Shp-SCB\SCB-boundary.shp')
```


