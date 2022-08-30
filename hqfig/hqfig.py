import matplotlib.pyplot as plt


def get_color_dict():
    COLOR_DICT = {
        'Azure'            : '#0096D9',
        'DarkCyan'         : '#0099AB',
        'DarkGoldenrod'    : '#AC640C',
        'DarkGray'         : '#9C9C9C',
        'DarkTurquoise'    : '#00D6C3',
        'GainsBoro'        : '#E6E6E5',
        'HoneyOrange'      : '#FABE6C',
        'IndianRed'        : '#C63F3D',
        'MediumAquamarine' : '#6CC6AB',
        'PrussianBlue'     : '#004C52',
        'SandBrown'        : '#F3A53D',
        'SaxeBlue'         : '#4EB397',
        'SeaGreen'         : '#2D745F',
        'Sepia'            : '#78312F',
        'SlateGray'        : '#6B798A',
        'StrongBlue'       : '#005F85',
        'Teal'             : '#007E74',
    }
    return COLOR_DICT


def get_color_list():
    color_dict = get_color_dict()
    return list(color_dict.values())


def setup(label_font=18, tick_font=16, axis_width=2, 
    tick_major_width=2, tick_minor_width=1.5, 
    tick_major_size=5, tick_minor_size=4, 
    showmajorticks=True, showminorticks=False):
    from matplotlib import rcParams
    # Conversion of unicode minus sign
    rcParams['axes.unicode_minus']=False
    # canvas setup
    rcParams['axes.labelsize']=label_font
    rcParams['axes.linewidth']=axis_width
    # x ticks setup
    rcParams['xtick.labelsize']=tick_font
    rcParams['xtick.direction']='in'
    rcParams['xtick.top']=True
    rcParams['xtick.minor.visible']=showminorticks
    rcParams['xtick.major.width']=tick_major_width
    rcParams['xtick.major.size']=tick_major_size if showmajorticks else 0
    rcParams['xtick.minor.top']=True
    rcParams['xtick.minor.width']=tick_minor_width
    rcParams['xtick.minor.size']=tick_minor_size
    # y ticks setup
    rcParams['ytick.labelsize']=tick_font
    rcParams['ytick.direction']='in'
    rcParams['ytick.right']=True
    rcParams['ytick.minor.visible']=showminorticks
    rcParams['ytick.major.width']=tick_major_width
    rcParams['ytick.major.size']=tick_major_size if showmajorticks else 0
    rcParams['ytick.minor.right']=True
    rcParams['ytick.minor.width']=tick_minor_width
    rcParams['ytick.minor.size']=tick_minor_size
    # font family
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Times New Roman']
    rcParams['mathtext.fontset'] = 'cm'


def main():
    setup_aesthetics()
    color = get_color_list()[0]

    import math
    x_arr = list(range(10))
    y_arr = [math.sin(x) for x in x_arr]

    plt.plot(x_arr, y_arr, '-o', color=color)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig('test.png', dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    main()
