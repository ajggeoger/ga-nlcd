''' 
    Constants info for Geoscience Australia NLCD dataset
    https://www.ga.gov.au/scientific-topics/earth-obs/accessing-satellite-imagery/landcover

    This file contains information relevant to the Collection (COLLECTION_ELEMENTS), items (ITEM_ELEMENTS) and information about the STAC extension (RASTERS).

'''


import pystac


# Info for NLCD
COLLECTION_ELEMENTS = {
        'title':
        'Dynamic Land Cover Dataset Version 2.1',
        'description':
        """
            The Dynamic Land Cover Dataset Version 2 is a suite of land cover information products from Geoscience Australia (GA). These information products deliver International Standards Organisation (ISO) compliant land cover maps across the Australian landmass. The datasets provide a consistent series of maps that show how Australian land cover is changing over time. The current version consists of 14 maps each based on 2 years of MODIS data. The 14 maps cover the period from January 2001 - December 2015. The Dynamic Land Cover Dataset uses a standard land cover classification to show the change in behaviour of land cover across Australia. The DLCD includes data for every 250m by 250m area on the ground, for the period 2001 to 2015. The DLDC provides a basis for reporting on change and trends in vegetation cover and extent. Information about land cover dynamics is essential to understanding and addressing a range of national challenges such as drought, salinity, water availability and ecosystem health. The current release of the second version DLCDv2.1 presents land cover information for every 250m by 250m area of the country. It consists of maps based on 2 years of MODIS EVI time-series data. DLCD can be used as an input for a wide range of environmental modelling applications. In conjunction with other data sources, the DLCD can be used to identify emerging patterns of land cover change and provide a spatial and historical context within which to interpret change. The land cover classification scheme used conforms to the 2007 International Standards Organisation (ISO) land cover standard (19144-2). The dataset shows Australian land covers clustered into 22 classes. These reflect the structural character of vegetation, ranging from cultivated and managed land covers (crops and pastures) to natural land covers such as trees and grasslands.
            """,
        'provider':
        pystac.Provider(name='Geoscience Australia',
                        url=('https://www.ga.gov.au/scientific-topics/earth-obs/accessing-satellite-imagery/landcover'),
                        roles=['producer', 'licensor']),
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[96.0, -46.0, 168.0, -9.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2001-01-01T00:00:00Z","2015-12-31T23:59:59Z"])
        ),
        'license':
        'Creative Commons Attribution 4.0 International Licence',
        'keywords':
        ['thematic data', 'Australia', 'land cover', 'environmental']
    }


# Info per asset
ITEM_ELEMENTS = {
    'DLCD_v2-1_MODIS_EVI_1_20020101-20031231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_1_20020101-20031231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2002-2003
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2002-01-01T00:00:00Z","2003-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_2_20030101-20041231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_2_20030101-20041231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2003-2004
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2003-01-01T00:00:00Z","2004-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_3_20040101-20051231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_3_20040101-20051231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2004-2005
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2004-01-01T00:00:00Z","2005-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_4_20050101-20061231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_4_20050101-20061231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2005-2006
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2005-01-01T00:00:00Z","2006-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_5_20060101-20071231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_5_20060101-20071231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2006-2007
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2006-01-01T00:00:00Z","2007-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_6_20070101-20081231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_6_20070101-20081231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2007-2008
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2007-01-01T00:00:00Z","2008-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_7_20080101-20091231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_7_20080101-20091231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2008-2009
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2008-01-01T00:00:00Z","2009-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_8_20090101-20101231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_8_20090101-20101231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2009-2010
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2009-01-01T00:00:00Z","2010-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_9_20100101-20111231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_9_20100101-20111231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2010-2011
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2010-01-01T00:00:00Z","2011-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_10_20110101-20121231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_10_20110101-20121231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2011-2012
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2011-01-01T00:00:00Z","2012-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_11_20120101-20131231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_11_20120101-20131231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2012-2013
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2012-01-01T00:00:00Z","2013-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_12_20130101-20141231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_12_20130101-20141231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2013-2014
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2013-01-01T00:00:00Z","2014-12-31T23:59:59Z"])
        )},
    'DLCD_v2-1_MODIS_EVI_13_20140101-20151231': {
        'id':
        'DLCD_v2-1_MODIS_EVI_13_20140101-20151231.tif',
        'description':
        """
            Land cover information for every 250m by 250m area of Australia for 2014-2015
            """,
        'extent': pystac.Extent(
            spatial=pystac.SpatialExtent([[110.0, -45.0047980, 155.0091890, -10.0]]),
            temporal=pystac.TemporalExtent(
                intervals=["2014-01-01T00:00:00Z","2015-12-31T23:59:59Z"])
        )}
}




#Info on rasters and STAC extension
RASTERS = {
    'spatial_resolution':
    0.002349,
    'nodata':
    0,
    "stac_extensions":
    "raster"
}