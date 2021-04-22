function [ ratingsCellArray ] = getMoodData(name, varargin)

%% collect some inputs
p = inputParser; p.KeepUnmatched = true;

p.addParameter('year', 2020);
p.addParameter('manualMoodFileName', []);
p.addParameter('normalizeMood', true, @islogical);



% Parse and check the parameters
p.parse(varargin{:});

%% Get the original CSV file
% If harry's computer, download a fresh copy
user = char(java.lang.System.getProperty('user.name'));
if strcmp(user, 'harrisonmcadams')
     % Code with my IP address here
    
    t = readtable(['~/Downloads/', name, 'MoodRatings.csv']);
    
else
    
    t = readtable(p.Results.manualMoodFileName);
    
end

%% Make datenum vector
datenumVector = datenum(strcat(num2str(t.Var1), '-', t.Var2, '-', sprintfc('%02d', t.Var3)), 'yyyy-mm-dd');

% Sort by date
[sortedDatenumVector, sortIndices ] = sort(datenumVector);

% Apply the sorting
ratings = t.Var5;
sortedRatings = ratings(sortIndices);

comments = t.Var6;
sortedComments = {comments{sortIndices}};

% Identify relevant rows based on desired year
if strcmp(p.Results.year, 'combined')
    beginningRow = 1;
    endingRow = length(sortedDatenumVector);
else
    [~, beginningRow] = min(abs(sortedDatenumVector - datenum(p.Results.year, 1, 1)));
    [~, endingRow] = min(abs(sortedDatenumVector - datenum(p.Results.year, 12, 31)));
end




%% Make the output
ratingsCellArray = [num2cell(sortedDatenumVector(beginningRow:endingRow)), num2cell(sortedRatings(beginningRow:endingRow)), {sortedComments{beginningRow:endingRow}}'];


end