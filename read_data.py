from argparse import ArgumentParser
import numpy as np
import matplotlib.pyplot as plt

def load_data(res_time, ground_data):
    result_x = []
    gold_x = []

    result_y = []
    gold_y = []

    for i in range(len(res_time)):
        result_x.append(res_time[i][11])
        result_y.append(res_time[i][3])
        gold_x.append(ground_data[i][11])
        gold_y.append(ground_data[i][3])
        
    return gold_x, gold_y, result_x, result_y


def plot_data(gold_data_x, gold_data_y, result_data_x, result_data_y):
    plt.scatter(gold_data_y, gold_data_x, s=0.1, c='red')
    plt.scatter(result_data_y, result_data_x, s=0.1, c='green')
    plt.scatter(gold_data_y[0], gold_data_x[0], s=0.1, c='black')
    plt.show()


if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-t", "--times", type=str, default=r"D:\University\Diplom\datasets\KITTY\data_odometry_gray\dataset\sequences\00\times.txt", help="Path to the times.txt in KITTI dataset")
    arg_parser.add_argument("-r", "--result", type=str, default=r"D:\University\Diplom\my_code\orbslam-windows-master\Examples\Results\Stereo\result_stereo_kitti_00.txt", help="Path to the KeyFrameTrajectory.txt file")
    arg_parser.add_argument("-e", "--exact", type=str, default=r"D:\University\Diplom\datasets\KITTY\data_odometry_poses\dataset\poses\00.txt", help="Path to the ground truth file")
    arg_parser.add_argument("-k", "--keyframes", type=str, default=r"D:\University\Diplom\my_code\orbslam-windows-master\Examples\Results\Stereo\key_frames_00.txt", help="Path to the key frames")

    args = arg_parser.parse_args()
    
    #Path to the times.txt in KITTI dataset
    ground_time = np.loadtxt(args.times)  
    #Path to the KeyFrameTrajectory.txt file
    res_time = np.loadtxt(args.result)  
    #Path to the ground truth file
    ground_data = np.loadtxt(args.exact)
    
    gold_data_x, gold_data_y, result_data_x, result_data_y = load_data(res_time, ground_data)
    plot_data(gold_data_x, gold_data_y, result_data_x, result_data_y)
