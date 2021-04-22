function plotCollapsedMood(ratingCellArray, varargin)
%% Parse inputs
p = inputParser; p.KeepUnmatched = true;

p.addParameter('saveName', []);
p.addParameter('normalize', false, @islogical);


% Parse and check the parameters
p.parse(varargin{:});


%% Pad ratings for missed days
counter = 1;
for ii = ratingCellArray{1,1}:ratingCellArray{end,1}
    dates(counter) = ii;
    
    relevantIndex = find([ratingCellArray{:,1}] == ii);
    
    if ~isempty(relevantIndex)
        paddedRatings(counter) = ratingCellArray{relevantIndex,2};
    else
        paddedRatings(counter) = NaN;
    end
    
    counter = counter + 1;
    
end

if p.Results.normalize
    paddedRatings = (paddedRatings - nanmean(paddedRatings))./nanstd(paddedRatings);
end

%% Do some plotting
% Reshape ratings into a 7xN size matrix where each column is a week
nWeeks = ceil(length(paddedRatings)/7);
paddedRatings(end+1:nWeeks*7) = NaN;
reshapedRatings = reshape(paddedRatings, [7,nWeeks]);

plotFig = figure;
imagesc(reshapedRatings, 'AlphaData',~isnan(reshapedRatings));
colorbar;
axisHandle = gca;
set(axisHandle,'TickLength',[0 0])
axisHandle.XTick = [];


% make the y axis labels
for ii = 1:7
    [~, dayOfWeek] = weekday(ratingCellArray{1,1}+ii-1);
    yLabel{ii} = dayOfWeek;
end

axisHandle.YTickLabels = yLabel;
axisHandle.DataAspectRatio = [1 1 1];

if ~isempty(p.Results.saveName)
    saveas(plotFig, p.Results.saveName);
end
end