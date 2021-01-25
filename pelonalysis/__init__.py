import pandas as pd
import matplotlib.pyplot as plt

def load_dataframe(csv_file='../data/data.csv'):
    """
    Load the peloton data file and create a time-based index based on the 'Workout Timestamp' column
    """
    data = pd.read_csv(csv_file)
    dates = data['Workout Timestamp'].map(lambda x: x[:16])
    data.loc[:, 'time'] = pd.to_datetime(dates)
    data.set_index('time', drop=True, inplace=True)
    return data

def filter_to_activity(data, activity):
    """
    filter the dataframe 'data' to include only the given activity
    """
    return data.loc[data['Fitness Discipline']==activity]

def filter_to_cycling(data):
    return filter_to_activity(data, 'Cycling')

def filter_to_running(data):
    return filter_to_activity(data, 'Running')

def filter_to_strength(data):
    return filter_to_activity(data, 'Strength')

def filter_to_ftp_tests(data):
    cyc = filter_to_cycling(data)
    return  cyc.loc[cyc['Title'] == '20 min FTP Test Ride', :]

def bucket_plot(data, ax, label='', field='Total Output'):
    """
    create a plot of the pandas dataframe 'data', drawing to the matplotlib axis `ax`.
    this shows the (default freq) weekly sum of the 'field', defaulting to total output on the bike.
    """
    weekly_sum = data[field].resample('W', label='right').sum();
    avg_weekly = weekly_sum.rolling(window=5).mean();
    title = f'{label} Weekly {field}'
    weekly_sum.plot(ax=ax, label=title)
    avg_weekly.plot(ax=ax, label=f'{title} smoothed')
    ax.legend()
    ax.set_title(title)

def ftp_plot(data, ax):
    """
    plot the total output from your cycling powerzone FTP tests
    """
    ftp = filter_to_ftp_tests(data)
    total_output = ftp['Total Output'].resample('W', label='right').sum()
    total_output = total_output[total_output>0]
    total_output.plot(
        ax=ax, 
        marker='o', 
        linestyle='', 
        markersize=20,
    )
    ax.set_title('FTP Test Output')

def barh_by_group(data, field='Fitness Discipline', **plot_args):
    """
    Show a sorted horizontal bar blot for the number of workouts by each category in the 'field' column
    """
    data.groupby(field).count()['Workout Timestamp'].sort_values().plot.barh(**plot_args);

def plot_workouts_vs_ftp(data, figsize=(15,15), **plot_args):
    """
    this is a cycling-focused plot showing both your weekly cycling output and total minutes (across all workouts)
    aligned with your ftp test results.
    """
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=figsize, **plot_args)
    (ax1, ax2, ax3) = axes
    bucket_plot(filter_to_cycling(data), ax1, 'Cycling')
    ftp_plot(data, ax3)
    bucket_plot(data, ax2, field='Length (minutes)')
    # ftp['Total Output'].resample('W', label='right').sum().plot(ax=ax2, marker='o', linestyle='', markersize=10, label='FTP Test Total Output')
    # ax2.legend();
    # ax2.set_ylim(350);
    # bucket_plot(df, ax3, field='Length (minutes)')
    fig, axes