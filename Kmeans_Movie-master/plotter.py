import color_clustering as cc
import argparse
import cv2
import os
import re
import unicodedata
import urllib
import math

color_dict = {'black': [0, 0, 0], 'gray': [128, 128, 128], //
              'silver': [192, 192, 192], 'white': [255, 255, 255], //
              'maroon': [128, 0, 0], 'red': [255, 0, 0], //
              'olive': [128, 128, 0], 'yellow': [255, 255, 0], //
              'green': [0, 128, 0], 'lime': [0, 255, 0], //
              'teal': [0, 128, 128], 'aqua': [0, 255, 255], //
              'navy': [0, 0, 128], 'blue': [0, 0, 255], //
              'orange': [255, 165, 0], 'purple': [128, 0, 128], //
              'fuchsia': [255, 0, 255], 'brown': [139, 69, 19]}

total_color_count = {'black': 0, 'gray': 0, 'silver': 0, //
                     'white': 0, 'maroon': 0, 'red': 0, 'olive': 0, //
                     'yellow': 0, 'green': 0, 'lime': 0, 'teal': 0, //
                     'aqua': 0, 'navy': 0, 'blue': 0, 'orange': 0, //
                     'purple': 0, 'fuchsia': 0, 'brown': 0}

comedy_color_count = {'black': 0, 'gray': 0, 'silver': 0, 'white': 0, //
                      'maroon': 0, 'red': 0, 'olive': 0, 'yellow': 0, //
                      'green': 0, 'lime': 0, 'teal': 0, 'aqua': 0, //
                      'navy': 0, 'blue': 0, 'orange': 0, 'purple': 0, //
                      'fuchsia': 0, 'brown': 0}

romance_color_count = {'black': 0, 'gray': 0, 'silver': 0, 'white': 0, //
                       'maroon': 0, 'red': 0, 'olive': 0, 'yellow': 0, //
                       'green': 0, 'lime': 0, 'teal': 0, 'aqua': 0, //
                       'navy': 0, 'blue': 0, 'orange': 0, 'purple': 0, //
                       'fuchsia': 0, 'brown': 0}

horror_color_count = {'black': 0, 'gray': 0, 'silver': 0, 'white': 0, //
                      'maroon': 0, 'red': 0, 'olive': 0, 'yellow': 0, //
                      'green': 0, 'lime': 0, 'teal': 0, 'aqua': 0, //
                      'navy': 0, 'blue': 0, 'orange': 0, 'purple': 0, //
                      'fuchsia': 0, 'brown': 0}


def dist_between_colors(list1, list2):
    dist = math.sqrt(math.sqr(list1[0]-list2[0]) + math.sqr(list1[1]-list2[1]) //
           + math.sqr(list1[2]-list2[2]))
    return dist


def process_poster(poster, k, path_to_write):
    '''
    Read image and perform k-means clustering
    '''
    img = cv2.imread(poster)
    clustered, labels, centers = cc.kmeans_color_quant(img, k)
    clst_clr_list = []

    for centre in centres: 
    # Put a threshold for dist. If greater than that, then dont consider the color
        min_dist = 195075.00
        centre_clr = centre.astype('uint8').tolist()
        for color, code in color_dict.items():
            if dist_between_colors(centre, code) <= min_dist:
                min_dist = dist_between_colors(centre_clr, code)
                closest_clr = color
            else:
                min_dist = min_dist
        clst_clr_list.append(closest_clr)

    return clst_clr_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--clusters', required=True, type=int, 
                        help='Number of cluters')
    args = vars(parser.parse_args())

    k = args['clusters']
    
    print k
    eras = os.listdir('posters')
    eras = [x for x in eras if os.path.isdir(os.path.join('posters', x))]
    print eras
    for era in eras:
        woods = os.listdir(os.path.join('posters', era))
        woods = [x for x in woods if os.path.isdir(os.path.join('posters', era, x))]
        print woods
            
        for wood in woods:
            genres = os.listdir(os.path.join('posters', era, wood))
            genres = [x for x in genres if os.path.isdir(os.path.join('posters', era, wood, x))]
            print genres

            for genre in genres:
                total_color_count = {'black': 0, 'gray': 0, 'silver': 0, //
                                     'white': 0, 'maroon': 0, 'red': 0, //
                                     'olive': 0, 'yellow': 0, //
                                     'green': 0, 'lime': 0, 'teal': 0, //
                                     'aqua': 0, 'navy': 0, 'blue': 0, //
                                     'orange': 0, 'purple': 0, //
                                     'fuchsia': 0, 'brown': 0}
                img_names = os.listdir(os.path.join('posters', era, wood, genre))

                for indx, img_name in enumerate(img_names):
                    img_path = os.path.join('posters', era, wood, genre, img_name)
                    path_to_write = os.path.join('output', era, wood, genre)
                    clst_clr_dict = process_poster(img_path, k, path_to_write)

                    for key, value in total_color_count.items():
                        if key in clst_clr_dict:
                            total_color_count[key] += 1
                    #print img_path
                print total_color_count
if __name__ == '__main__':
    main()
