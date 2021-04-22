function analyzeExercise(ratingCellArray, varargin)
p = inputParser; p.KeepUnmatched = true;

p.addParameter('saveName', []);
p.addParameter('additionalExerciseKeyWords', {}, @iscell);
p.addParameter('additionalFakeExerciseKeyWords', {}, @iscell);


% Parse and check the parameters
p.parse(varargin{:});

%% Find relevant indices
exerciseKeyWords = {'exercise', 'worked out', 'working out', 'work out', 'workout', 'run', 'yoga', 'madfit', 'abs'};
exerciseKeyWords = {exerciseKeyWords{:}, p.Results.additionalExerciseKeyWords{:}};
totalExerciseIndices = [];
for ii = 1:length(exerciseKeyWords)
    exerciseIndices = find(contains({ratingCellArray{:,3}},exerciseKeyWords{ii}, 'IgnoreCase', true));
    totalExerciseIndices = [totalExerciseIndices, exerciseIndices];
end
totalExerciseIndices = unique(totalExerciseIndices);

nonExerciseKeyWords = {'not working out', 'not work out', 'no exercise'};
nonExerciseKeyWords = {nonExerciseKeyWords{:}, p.Results.additionalFakeExerciseKeyWords{:}};
totalFakeExerciseIndices = [];
for ii = 1:length(nonExerciseKeyWords)
    fakeExerciseIndices = find(contains({ratingCellArray{:,3}},nonExerciseKeyWords{ii}, 'IgnoreCase', true));
    totalFakeExerciseIndices = [totalFakeExerciseIndices, fakeExerciseIndices];
end
totalFakeExerciseIndices = unique(totalFakeExerciseIndices);

% Remove fakes
totalExerciseIndices = setxor(totalExerciseIndices, totalFakeExerciseIndices);

totalIndices = (1:length({ratingCellArray{:,2}}));
nonExerciseIndices = setxor(totalIndices, totalExerciseIndices);

%% Grab appropriate ratings
exerciseRatings = [ratingCellArray{totalExerciseIndices,2}];
nonExerciseRatings = [ratingCellArray{nonExerciseIndices,2}];

%% Plot results
data = nan(length(totalIndices), 2);
data(1:length(exerciseRatings),1) = exerciseRatings;
data(1:length(nonExerciseRatings),2) = nonExerciseRatings;

plotFig = figure;
hold on;
plotSpread_scatter(data, 'spreadWidth', 0.5, 'distributionMarker', '.', 'markerSize', 1000, 'alpha', 0.2);
boxplot(data, 'Labels', {'Exercise Days', 'Non-Exercise Days'});
ylabel('Mood Rating');

[h,probability,ci,stats] = ttest2(exerciseRatings, nonExerciseRatings);
title(['Exercise (N = ', num2str(length(exerciseRatings)), ', ', sprintf('%4.2f', 100*length(exerciseRatings)/(length(exerciseRatings)+length(nonExerciseRatings))), '%) vs. Non-Exercise (N = ',num2str(length(nonExerciseRatings)), ', ', sprintf('%4.2f', 100*length(nonExerciseRatings)/(length(exerciseRatings)+length(nonExerciseRatings))), '%): ', sprintf('%4.3f', mean(exerciseRatings)), ' vs. ', sprintf('%4.3f', mean(nonExerciseRatings)), ' , p = ', sprintf('%4.3f', probability)]);


if ~isempty(p.Results.saveName)
    saveas(plotFig, p.Results.saveName);
end

end