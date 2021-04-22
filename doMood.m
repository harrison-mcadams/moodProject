close all;

%% Set some parameters

name = 'harry';
%name = 'geena';

%year = 2020;
year = 2021;
%year = 'combined';

saveDir = '~/Desktop';
saveNameSuffix = ['_',num2str(year), '_', name, '.png'];

%% Get the data

[ ratingCellArray ] = getMoodData(name, 'year', year);

%% Do some analysis

saveName = fullfile(saveDir, ['ratingByDayOfWeek', saveNameSuffix]);
analyzeByDayOfWeek(ratingCellArray, 'saveName', saveName);

saveName = fullfile(saveDir, ['exercise', saveNameSuffix]);
analyzeExercise(ratingCellArray, 'saveName', saveName);